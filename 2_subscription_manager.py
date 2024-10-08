subscribers = []


def subscribe(name):
    subscribers.append(name)

    def confirm_subscription():
        return f"Subscription confirmed for {name}"

    print(confirm_subscription())


def unsubscribe(name):
    if name in subscribers:
        subscribers.remove(name)
        return f"{name} successfully unsubscribed"
    else:
        return f"{name} not found in subscriber list"


subscribe("Denys")
subscribe("Nick")
subscribe("Taylor")
print(*subscribers)

print(unsubscribe("Denys"))
print(*subscribers)

print(unsubscribe("Sergiy"))