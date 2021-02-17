
if [ "$#" == "0" ]; then
	database=('Notebooks' 'Printers' 'Desktops' 'Tablets' 'Gaming' 'Software')
else
	database="$@"
fi

cd $(dirname "$0")

for dataset in ${database[*]}; do

	printf "\n${dataset}\n"

	python3 main.py ${dataset} --url

done

for times in $(seq 1 3); do

	printf "\n%s\n" "------------------------------"

	for dataset in ${database[*]}; do

		printf "\n${dataset}\n"

		python3 main.py ${dataset} --html

	done

done
