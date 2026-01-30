from supabase import create_client

# MUST have trailing slash
SUPABASE_URL = "https://yeyzazawudczsbckghrr.supabase.co/"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InlleXphemF3dWRjenNiY2tnaHJyIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Njk3NTE0ODEsImV4cCI6MjA4NTMyNzQ4MX0.wK99MJ-ZDdxMo-pvFBKEM-CS6zZ6gSp_L5_-cHwPgeg"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

bucket_name = "imgs2"
file_path = "cat.png"    # make sure this file exists
file_name = "cat.png"

with open(file_path, "rb") as f:
    supabase.storage.from_(bucket_name).upload(
        path=file_name,
        file=f,
        file_options={
            "content-type": "image/png"
        }
    )

print("✅ Image uploaded")

url = supabase.storage.from_(bucket_name).get_public_url(file_name)
print("✅ Public URL:")
print(url)
