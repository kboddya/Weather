run:
	py main.py

set_url:
	git remote set-url origin https://bokoyolo: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@github.com/bokoyolo/Weather.git

commit:
	git add .
	git commit -m "Fix main.py: Add none stop bot polling"

push:
	git  push  origin master


down:
	heroku ps:scale worker=0

deploy:
	heroku ps:scale worker=1
	git push heroku master

logs:
	heroku logs --tail

.DEFAULT_GOAL := run
