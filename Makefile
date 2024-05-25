all: Draft
	@echo "Compilation terminated"

clean:
	rm Draft.o Draft

Draft: Draft.o
	gcc -o Draft Draft.o

Draft.o: draft.c
	gcc -c -Wall -O3 draft.c

execute : all
	./Draft