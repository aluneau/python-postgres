# Create venv 
```
python3 -m venv myenv 
source myenv/bin/activate
```
# Install dependencies
```
pip install -r requirements.txt
```

# Start postgres
```
podman run --name some-postgres \
  -e POSTGRES_USER=myuser \
  -e POSTGRES_PASSWORD=mysecretpassword \
  -e POSTGRES_DB=mydatabase \
  -p 5432:5432 \
  -d postgres

```

# Execute the app
```
uvicorn main:app --reload
```
