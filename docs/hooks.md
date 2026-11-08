# Hooks reference

Configuration: [`hooks/hooks.json`](../hooks/hooks.json). Implementation:
[`hooks/scripts/guard.py`](../hooks/scripts/guard.py) (Python 3, standard library only).

| Event | Matcher | Mode | Purpose |
|---|---|---|---|
| `PreToolUse` | `Bash` | `guard.py bash` | Safety rules, read-only agents, cost guard for `cat` |
| `PreToolUse` | `Read\|Edit\|Write\|MultiEdit\|NotebookEdit` | `guard.py files` | Secret files, read-only agents, cost guard |
| `SessionStart` | `startup\|resume\|clear\|compact` | `guard.py progress` | Loads `PROGRESS.md` into context |

A block exits with code 2 and puts the reason on stderr. Claude Code stops the tool call and shows
Claude the reason. Any internal error exits 0, so a guard bug can never break a session.

## Bash rules

| Rule | Example blocked | Example allowed |
|---|---|---|
| Recursive delete of root, home or the whole working dir | `rm -rf /`, `rm -rf ~`, `rm -rf .` | `rm -rf target build` |
| Force push | `git push --force`, `git push -f`, `git push origin +branch` | `git push --force-with-lease` |
| Irreversible cleanup | `git clean -fdx` | `git clean -n` |
| Destructive SQL anywhere in the line | `psql -c "DROP TABLE users"` | `psql -c "SELECT 1"` |
| `kubectl delete` | `kubectl delete pod x` | `kubectl get pods` |
| Mutating kubectl/helm against production | `kubectl --context eks-prod apply -f x.yaml`, `helm upgrade ... --kube-context eks-prod` | the same against `dev` |
| Terraform destroy / auto-approve | `terraform destroy`, `terraform apply -auto-approve` | `terraform plan`, interactive `apply` |
| Mutating AWS CLI with a production profile | `aws ec2 terminate-instances --profile prod-admin` | `aws ec2 describe-instances --profile prod-admin` |
| Shell reads of secret files | `cat .env`, `cat ~/.aws/credentials` | `cat .env.example` |

When no `--context` or `--kube-context` flag is given, the current kubectl context is looked up
(3-second timeout). A namespace containing the production pattern also counts as production.

## Read-only agents

`READ_ONLY_AGENTS = {k8s-debugger, incident-triage, security-reviewer, performance-reviewer,
spring-conventions-reviewer, doc-explorer}`

For these agents (detected from the hook input's `agent_type`, with or without the plugin namespace),
the following are also blocked: any mutating kubectl/helm/terraform/AWS command, `git`
commit/push/reset/rebase/merge/checkout/clean/stash/tag/cherry-pick/revert/apply, `rm`, `mv`,
`chmod`, `chown`, `dd`, `truncate`, `sed -i`, and the Edit/Write/MultiEdit/NotebookEdit tools.

## Secret file patterns

File names: `.env`, `.env.*` (except `.example`, `.sample`, `.template`, `.dist`), `*.pem`, `*.key`,
`*.p12`, `*.pfx`, `*.jks`, `*.keystore`, `id_rsa`/`id_dsa`/`id_ecdsa`/`id_ed25519` (and `.pub`),
`.git-credentials`, `.npmrc`, `.pypirc`, `.netrc`, `*-service-account.json`,
`application_default_credentials.json`.

Paths: `.aws/credentials`, `.kube/config`, `.docker/config.json`, `.ssh/`, `.azure/`, `.config/gcloud/`.

## Cost guard

- Generated or vendored directories: `node_modules`, `target`, `build`, `dist`, `out`, `.gradle`,
  `.mvn/wrapper`, `.next`, `coverage`, `__pycache__`, `.venv`, `venv`, `.terraform`.
- Noise files: `*.min.js`, `*.min.css`, `*.map`, `package-lock.json`, `yarn.lock`, `pnpm-lock.yaml`,
  `*.jar`, `*.class`.
- Large files: over 512 KB (`LARGE_FILE_BYTES`) read whole with Read (no `offset`/`limit`) or with
  `cat`/`less`/`more`/`bat`.
- Edits and writes to generated folders are not blocked; only reads are.
- Disable for a session with `ADT_COST_GUARD=off claude`.

## Production pattern

```python
PROD_RE = re.compile(r"prod|prd|live", re.IGNORECASE)
```

Change it to match your naming, for example `r"(^|-)prod(-|$)|^p-"`, then run
`python3 tests/test_guard.py`.
