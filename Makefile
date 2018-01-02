package:
	rm -f kreader.zip
	zip kreader.zip kreader.py
	rm -f pizza.zip
	zip pizza.zip pizza.py

deploy:
	aws s3 cp kreader.zip s3://$(DEPLOY_BUCKET)
	aws s3 cp pizza.zip s3://$(DEPLOY_BUCKET)
