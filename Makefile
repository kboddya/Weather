run:
	py main.py

set_url:
	git push https://<GITHUB_ACCESS_TOKEN>@github.com/<GITHUB_USERNAME>/<REPOSITORY_NAME>.git

commit:
	git add .
	git commit -m "Fix main.py: Add none stop bot polling"

push:
	git push https://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@github.com/bokoyolo/Weather.git


down:
	heroku ps:scale worker=0

deploy:
	heroku ps:scale worker=1
	git push heroku master

logs:
	heroku logs --tail

.DEFAULT_GOAL := run
