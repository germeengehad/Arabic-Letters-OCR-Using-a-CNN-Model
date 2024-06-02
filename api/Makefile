include ../.env
export $(shell sed 's/=.*//' ../.env)

clean:

build:
	@docker image rm --force $(HUB_URL)/$(APP_NAME_BACKEND):$(APP_VERSION) || true
	@docker build -t ${HUB_URL}/$(APP_NAME_BACKEND):$(APP_VERSION) --build-arg VERSION=$(IMAGE_VERSION) .

publish:
	@docker login ${HUB_URL}
	@docker push ${HUB_URL}/$(APP_NAME_BACKEND):$(APP_VERSION)

lint:
	@docker run --rm -i hadolint/hadolint < Dockerfile
