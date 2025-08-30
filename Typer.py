from Tclass import typer
words=typer.give_words()
print(f"your sentence is {words}")
time_taken,user_type=typer.type_speed()
counter=typer.valid(user_type,words)
print(f"{typer.accuracy(counter,words):.2f}% accuracy")
print(f"Time taken: {time_taken:.2f} sec")
print(f"{counter/time_taken*60:.2f} wpm")