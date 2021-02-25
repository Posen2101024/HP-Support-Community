
cd $(dirname "${0}")

download() {

	# id = ${1}

	gdown "https://drive.google.com/uc?export=download&id=${1}" -O model.zip

	unzip -o database.zip && rm database.zip
}

download "1Zw4jQsdGDk3Eirx3cThDPgB3hLZSydgy"
