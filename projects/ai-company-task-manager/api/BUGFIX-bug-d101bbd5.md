# Bug Fix Notes

Bug: 감사 로그에 actor 누락
Root cause: Audit writer omitted required actor field in first impl seed
Fix: require actor in PATCH status payload; persist on audit row
Regression test: assert actor present
Date: 2026-07-15
