COLOR := "\e[1;36m%s\e[0m\n"

.PHONY: run, lint-black, clean
run: ## Run Journey Viz Dashboard with Hot Reload
	@printf $(COLOR) "Running docker-compose..."
	@docker-compose up

#poetry black all files

lint-black: ## Lint code with black
	@printf $(COLOR) "Running black..."
	@poetry run black .


clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	rm -rf .pytest_cache/
