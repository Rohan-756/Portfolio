
    public_url =  supabase.storage.from_(bucket_name).get_public_url(
  image_path
)
    print(f"Public URL of the image: {public_url}")
except Exception as e:
    print(f"Error getting public URL: {e}")