from django.dispatch import Signal


friendship_request_status_changed = Signal(
    providing_args=[
        "friendship_request",
        "attributes"
    ]
)


friendship_request_declined = Signal(
    providing_args=[
        "friendship_request",
        "attributes"
    ]
)


friendship_request_canceled = Signal(
    providing_args=[
        "friendship_request",
        "attributes"
    ]
)