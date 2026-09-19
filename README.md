# jarvis-sandbox

A deliberately tiny repository for exercising Jarvis's `github_propose_code_change`
and `github_open_pull_request` tools end to end.

Nothing here is used by anything. The code is small on purpose: one file, two
functions, no dependencies, so a proposed edit is easy to read and a wrong edit
is obvious.

## The known defect

`apply_discount` does not clamp. With `percent_off` above 100 it returns a
negative price:

    apply_discount(1000, 150)  ->  -500

A price should never be negative, and a discount above 100% should be treated
as 100%.

---

_This pull request was opened from a Jira ticket (TESTP-605), not from Slack._
