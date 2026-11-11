\---

name: c

description: >-

&#x20; Commit every change in the repo and push it to GitHub in one pass. Use when

&#x20; the user runs /c, asks to commit and push, or wants everything sent to

&#x20; GitHub. Always stage the full working tree (minus secrets and junk), commit

&#x20; once, and push — unless the user opts out with --no-push or names specific paths.

disable-model-invocation: true

\---

\# Commit



Send \*\*everything changed in the repo\*\* to GitHub in \*\*one fell swoop\*\*: wait until every agent in this conversation is finished, then inspect, stage the full working tree, commit once, and push — no stop-and-ask between steps.



\*\*Standing preference:\*\* `/c` means the whole repo, commit \*\*and\*\* push. Do not ask "should I push?" or "commit the rest too?" Do not limit the commit to files from the current chat.



\## Parse



Accept `/c` with optional flags:



| Input | Behavior |

|-------|----------|

| `/c` | Stage the entire working tree, one commit, push |

| `/c --no-push` | Stage the entire working tree, commit only |

| `/c path/to/file` | Stage only named paths, commit, push |

| `/c push` | Same as `/c` (push is default) |

| Clean tree | Report nothing to commit; do not push |



If the user says "commit but don't push", honor `--no-push`.



\## Wait for all agents (before push)



Do \*\*not\*\* push while other agent work for this conversation may still be running. Do not commit either: a commit taken early would miss files those agents are still writing, and the push would send an incomplete tree.



\*\*Running work includes:\*\*



\- Background \*\*Task\*\* / subagent runs started in this chat that have not yet returned a completion (system notification or tool result).

\- Cloud or background agents the user started from this thread that are not finished.

\- Another turn still executing long-running shell work that will change the repo, when you know it is in flight.



\*\*How to decide:\*\*



1\. Scan the conversation for subagent launches vs completions. If any ID or worker was started and never completed, treat it as \*\*still running\*\*.

2\. If the user just sent `/c` while workers are active: reply in one short line (count or names if known) that you are \*\*waiting for agents to finish before pushing\*\*, then \*\*end the turn\*\*. Do not stage, commit, or push.

3\. When `/c` is invoked again — or you are woken after the last worker completes — and nothing is in flight, continue with inspect, commit, and push.



Do \*\*not\*\* use sleep loops or busy-polling to block on subagents. Either proceed when quiescent or end the turn and let Cursor wake you when work completes.



If the user says agents are done but the transcript still shows a running worker, trust the transcript and keep waiting.



\## One-fell-swoop rule (critical)



When the user runs `/c`:



1\. \*\*Stage the whole working tree\*\* — every modified and untracked file that belongs in git, including work from other chats, other tasks, and files you did not touch. Do not leave "unrelated" project files uncommitted.

2\. \*\*One commit\*\* — a single commit for the whole working tree. Do not split by theme and do not ask whether to commit the rest.

3\. \*\*Push immediately\*\* after a successful commit — same turn, no confirmation prompt.



Only commit a subset when the user names specific paths (`/c path/to/file`). Then say what was left out. Secrets and junk listed under "What to stage" stay out; say what you excluded.



\## Safety (always)



\- \*\*Never\*\* update git config

\- \*\*Never\*\* run destructive git commands (`push --force`, `reset --hard`, etc.) unless the user explicitly asks

\- \*\*Never\*\* skip hooks (`--no-verify`, `--no-gpg-sign`) unless explicitly requested

\- \*\*Never\*\* force-push to `main`/`master` — warn first

\- \*\*Never\*\* `git commit --amend` unless all amend rules are met (user asked, your commit, not pushed)

\- \*\*Never\*\* commit secrets (`.env`, `secrets.toml`, credentials, tokens) — warn and exclude

\- \*\*Never\*\* create an empty commit when there are no changes



\## Workflow



\### 1. Inspect (parallel)



Run these together:



```bash

git status --short

git diff HEAD

git log -5 --oneline

git status -sb

```



Also check:



\- Full list of modified and untracked files — all of them go in unless they are secrets or junk

\- Whether the branch tracks a remote and is ahead/behind

\- Recent commit message style in this repo



\### 2. Draft message



Write a \*\*1–2 sentence\*\* message focused on \*\*why\*\*, covering the whole changeset.



\- Lead with type when obvious: `fix`, `feat`, `refactor`, `test`, `docs`, `chore`

\- Match the repo's existing tone from `git log`

\- Accurate verbs: `add` = new feature, `fix` = bug, `update` = enhancement, `remove` = deletion

\- Optional second paragraph (body) for context the subject line can't carry

\- If multiple themes are bundled, use a broad subject plus a body that lists the main themes



\*\*Examples:\*\*



```

Remove unused code and legacy scripts to reduce maintenance surface.



Delete dead helpers and superseded manual test scripts now covered by pytest.

```



```

fix(invoices): preserve draft when returning from client edit



Store return context in session state so unsaved line items are not lost.

```



Briefly show the proposed subject (+ body if any) before committing unless the user said to just do it.



\### 3. Stage and commit (all at once)



Stage the whole repo, then commit:



```bash

git add -A

git commit -m "Subject line." -m "Optional body paragraph."

```



`git add -A` is the default. After staging, unstage anything that must stay out (secrets, cache, build junk) with `git restore --staged`. Do not hand-pick "this chat's files" and leave the rest dirty.



\*\*PowerShell:\*\* use multiple `-m` flags. Do \*\*not\*\* use bash heredocs (`<<'EOF'`) — they fail in PowerShell.



If pre-commit hooks fail: fix the issue and create a \*\*new\*\* commit (do not amend a failed commit).



\### 4. Push to GitHub (required — same turn)



Immediately after a successful commit, push unless the user used `--no-push`.



```bash

git push

```



If the branch has no upstream:



```bash

git push -u origin HEAD

```



Use `gh` when helpful (`gh repo view`, `gh auth status`) but prefer plain `git push` for updates.



Do \*\*not\*\* end `/c` with:

\- only a local commit

\- a question about pushing

\- uncommitted project files still on disk



\### 5. Confirm



Report in one summary:



\- Commit hash and subject

\- Push result: remote branch and range (e.g. `abc1234..def5678` on `origin/main`), or that push was skipped because the user opted out

\- Any files intentionally excluded (secrets or cache artifacts only)



\## What to stage



\*\*Include by default:\*\* every modified and untracked file in the repo — source, tests, configs, docs, images, and work that did not come from this chat.



\*\*Always exclude unless the user asks:\*\*



\- `.env`, `secrets.toml`, credentials, API keys

\- `.pytest\_cache/`, `\_\_pycache\_\_/`, `.pyc`, build artifacts, IDE-local junk



There is no "unrelated local edits" exclusion. If it is in the working tree and it is not a secret or junk, it goes in the commit and gets pushed.



\## Push failures



| Error | Action |

|-------|--------|

| Branch behind remote | `git pull --rebase`, resolve conflicts, push again |

| No upstream | `git push -u origin HEAD` |

| Auth failed | Report; suggest `gh auth login` or checking credentials |

| Force push required | Stop and ask — never force-push `main`/`master` silently |



\## Do not



\- Commit only the current chat's files and leave the rest of the working tree dirty

\- Ask whether to commit or push the rest after `/c`

\- Stop after commit without pushing (unless `--no-push`)

\- Split the working tree into several commits because the themes differ — one commit, and mention the themes in the body

\- Push when user used `--no-push`

\- Run extra exploration commands beyond git/gh needed for this workflow

\- Use `git commit -i` or other interactive git commands



