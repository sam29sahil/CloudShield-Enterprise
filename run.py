from app import create_app

app = create_app()

<<<<<<< HEAD
print("\n========== ROUTES ==========")
for rule in app.url_map.iter_rules():
    print(f"{rule.endpoint:35} -> {rule}")
print("============================\n")
print("\n===== REGISTERED ROUTES =====")
for rule in app.url_map.iter_rules():
    print(rule)
print("=============================\n")


=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
if __name__ == "__main__":
    app.run(debug=True)