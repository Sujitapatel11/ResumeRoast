CareerOS Master Blueprint
Part 4 – Database Design
1. Database Philosophy
Use PostgreSQL as the single source of truth. Tables represent business entities, not technologies.
Normalize where appropriate while keeping queries practical.
2. Core Entity Relationships
User
nnn CareerProfile
nnn Resume
n nnn ResumeVersion
n nnn ResumeAnalysis
nnn Roadmap
n nnn LearningTask
nnn Application
n nnn Interview
nnn Contribution
nnn Subscription
3. Database Tables
users: Stores authentication, identity, role, status.
career_profiles: Career goals, skills, education, experience, preferred companies.
resumes: Resume metadata and MinIO object reference.
resume_versions: Every generated version of a resume.
resume_analyses: ATS score, roast, missing skills, AI insights.
companies: Company profile, hiring trends, interview metadata.
job_postings: Imported or user-selected job descriptions.
roadmaps: Generated career roadmap.
learning_tasks: Daily/weekly learning tasks linked to roadmap.
applications: Tracks application lifecycle.
interviews: Interview rounds, feedback and scores.
contributions: Community interview reports and hiring signals.
subscriptions: User plan, billing status, limits.
notifications: Email and in-app reminders.
audit_logs: Security and important system events.
4. Key Relationships
One User fi Many Resumes
One Resume fi Many Resume Versions
One Resume fi Many Analyses
One User fi Many Applications
One Application fi Many Interviews
One Roadmap fi Many Learning Tasks
One User fi Many Contributions
5. Primary Keys
Every table uses a unique id (UUID or integer depending on implementation). Foreign keys
maintain referential integrity.
6. Indexing Strategy
Index:
email
company_id
user_id
resume_id
application_id
created_at
status
These support fast lookups and filtering.
7. Storage Strategy
Structured data fi PostgreSQL
Resume PDFs fi MinIO
Temporary cache fi Redis
8. Data Integrity Rules
Foreign keys enabled.
Soft delete where appropriate.
Audit timestamps on major entities.
Validation before persistence.
9. Future Evolution
Later versions may split analytics, AI history and community into separate databases only when
scale justifies it.
10. CTO Decision Record
Accepted: PostgreSQL, normalized business entities, object storage for files.
Rejected: MongoDB-first design, storing PDFs in database, duplicate user data