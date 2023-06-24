.phony: serve-videos


HOST := 0.0.0.0
PORT := 6969
VIDEOS_DIR := "videos"

serve:
	python -m http.server --bind $(HOST) $(PORT)

