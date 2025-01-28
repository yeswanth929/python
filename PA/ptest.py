def summarize_items(person_name, *args, **kwargs):
    print(f"Name: {person_name}")
    print(f"number of items: {len(args)}")
    return kwargs
result = summarize_items(
    "YP", 
    1,2,3,"moofasa",
    date="2025-01-27", location="kansas city", event="practice_Workshop"
)
print("Keyword arguments as dictionary:", result)
