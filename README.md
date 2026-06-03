# zen_back

Zentodo backend application.

## Deploy to Vercel

1. Push this repository to GitHub.
2. Import the repository in Vercel as a Python/Django project.
3. Add these environment variables in Vercel:
   - `SECRET_KEY`: a long random Django secret.
   - `DEBUG`: `False`.
   - `ALLOWED_HOSTS`: `.vercel.app,your-domain.com` if you use a custom domain.
   - `CSRF_TRUSTED_ORIGINS`: `https://*.vercel.app,https://your-domain.com`.
   - `DATABASE_URL`: your production Postgres connection string.
4. Deploy.
5. Run migrations against the production database from your local machine:

```powershell
$env:DATABASE_URL="your-production-postgres-url"
python manage.py migrate
```

Vercel serverless functions are not a good place for SQLite writes, webcam access, or YOLO/OpenCV processing. This deployment config is for the Django todo API.
