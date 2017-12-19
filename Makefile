package:
	rm -f kreader.zip
	zip kreader.zip kreader.py

deploy:
	aws s3 cp kreader.zip s3://$(DEPLOY_BUCKET)
