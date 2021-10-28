run:
	py main.py

set_url:
	git remote set-url origin https://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@github.com/bokoyolo/Weather.git

commit:
	git add .
	git commit -m "Fix main.py: Add none stop bot polling"

push: commit
	git push origin master

down:
	heroku ps:scale worker=0

deploy: commit
	heroku ps:scale worker=1
	git push heroku master

.DEFAULT_GOAL := run
