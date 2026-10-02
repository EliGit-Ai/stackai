# StackAI Readiness Scoring Rubric

Score each dimension 0, 1, or 2. Base every score on user evidence.

## 1. Business objective

**0** — No meaningful objective after clarification.  
**1** — General direction but no bounded first use case.  
**2** — Clear, practical first use case with expected business value.

## 2. System and source-code availability

**0** — No reliable source access or system cannot be accessed for the pilot.  
**1** — Partial access, incomplete repository, or access depends on another party.  
**2** — Relevant repository/source and basic system information are accessible.

## 3. Ownership of technical assets

**0** — Critical assets are vendor-only, unknown, or not under business control.  
**1** — Mixed ownership/control; business has some access but material dependency remains.  
**2** — Business controls core repository/accounts and vendors receive scoped access.

## 4. Responsible internal owner

**0** — No internal owner.  
**1** — Candidate exists but role/authority is unclear.  
**2** — Named internal owner can coordinate the pilot and make access/process decisions.

## 5. Development/Test environment and rollback

**0** — Production-only and/or no reliable rollback.  
**1** — Partial safe environment or rollback capability.  
**2** — Separate Dev/Test plus Git/backup/rollback suitable for a controlled pilot.

## 6. Access and permissions governance

**0** — Shared admin access, unknown permissions, vendor-only control, or uncontrolled credentials.  
**1** — Some individual accounts and access controls exist but are incomplete.  
**2** — Named identities, least privilege, business-controlled access, and reviewable permissions.

## 7. Security, sensitive data, secrets and credentials

**0** — Sensitive data/secrets exist with no mapping or unsafe handling.  
**1** — Risks are known but controls are partial/inconsistent.  
**2** — Sensitive data is mapped, secrets are separated, and access controls are defined.

## 8. Ongoing support and operational ownership

**0** — No plan for updates, access, troubleshooting, or offboarding.  
**1** — Ad-hoc owner/support exists but process is incomplete.  
**2** — Clear operating owner and process for support, access changes, updates, and offboarding.

# Total score

Maximum: 16.

- **13–16** — Ready for a Claude Code pilot
- **9–12** — Ready after limited preparation
- **5–8** — Infrastructure and governance preparation required
- **0–4** — Start with technical and ownership mapping

# Scoring guardrails

- A non-technical business owner is not a readiness defect.
- External development is not a readiness defect by itself.
- Do not infer ownership from access.
- Do not infer safe rollback merely because Git exists.
- Unknown facts should remain unknown until clarified.
- Critical blockers are reported separately and can restrict the recommended pilot even with a high score.