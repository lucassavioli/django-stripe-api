import stripe
import os
from dotenv import load_dotenv
from rest_framework.views import APIView

load_dotenv()

stripe.api_key = os.environ.get("STRIPE_SECRET_KEY")


class StripeCheckoutView(APIView):
    def post(self, request):
        try:
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        "price": "price_1Os6lMBli90o6fIcW2qOpZhJ",
                        "quantity": 1,
                    },
                ],
                payment_method_types=["card"],
                mode="payment",
                success_url=YOUR_DOMAIN + "?success=true",
                cancel_url=YOUR_DOMAIN + "?canceled=true",
            )
        except Exception as e:
            return str(e)

        return redirect(checkout_session.url, code=303)
