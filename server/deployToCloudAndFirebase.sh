gcloud config set project cravern
gsutil -m rsync -r ./src/templates/static gs://cravern/static
gcloud builds submit --tag gcr.io/cravern/cravern
gcloud beta run deploy cravern --image gcr.io/cravern/cravern --platform managed --region us-central1