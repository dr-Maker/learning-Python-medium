import data


def main():
    
    all_python_devs = [ worker["name"] for worker in data.Info if worker["language"] == "python" ]
    # print(all_python_devs)

    adults = list(filter(lambda worker: worker["age"] > 18 , data.Info))
    adults = list(map(lambda worker: worker["name"], adults))
    # print(adults)


    old_people = list(map(lambda work: {**work ,**{"old": work["age"] > 50 }}, data.Info))
    print(old_people)



if __name__ == "__main__":
    main()