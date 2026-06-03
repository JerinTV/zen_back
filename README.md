# zen_back

Zentodo backend application.

## Deploy to Vercel

1. Push this repository to GitHub.
2. Import the repository in Vercel as a Python/Django project.
3. Add these environment variables in Vercel:
   - `SECRET_KEY`: a long random Django secret.
   - `DEBUG`: `False`.
   - `ALLOWED_HOSTS`: `.vercel.app,your-domain.com` if you use a custom domain.
   - `CSRF_TRUSTED_ORIGINS`: `https://*.vercel.app,https://todo-blond-psi.vercel.app,https://todo-jerintvs-projects.vercel.app,https://todo-jerintv-jerintvs-projects.vercel.app,https://your-domain.com`.
   - `CORS_ALLOWED_ORIGINS`: `https://todo-blond-psi.vercel.app,https://todo-jerintvs-projects.vercel.app,https://todo-jerintv-jerintvs-projects.vercel.app,http://localhost:3000,http://127.0.0.1:3000`.
   - `SIMPLE_JWT_SIGNING_KEY`: a long random JWT signing secret, or omit it to reuse `SECRET_KEY`.
   - `DATABASE_URL`: your production Postgres connection string. This is required on Vercel; SQLite cannot be used for production writes there.
4. Deploy.
5. Run migrations against the production database from your local machine:

```powershell
$env:DATABASE_URL="your-production-postgres-url"
python manage.py migrate
```

Vercel serverless functions are not a good place for SQLite writes, webcam access, or YOLO/OpenCV processing. This deployment config is for the Django todo API.

## Frontend API URL

The frontend should use `REACT_APP_API_BASE_URL=https://zentodobackend.vercel.app/api/` for production builds.
