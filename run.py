from app import create_app

app = create_app()

<<<<<<< HEAD
print("\n========== ROUTES ==========")
for rule in app.url_map.iter_rules():
    print(f"{rule.endpoint:35} -> {rule}")
print("============================\n")
=======
print("\n===== REGISTERED ROUTES =====")
for rule in app.url_map.iter_rules():
    print(rule)
print("=============================\n")
>>>>>>> 85b73280dbe0ae93cb04b6fe019fa37bd58bbd40

if __name__ == "__main__":
    app.run(debug=True)