import stripe
import os
from django.conf import settings
from dotenv import load_dotenv
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import redirect

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
                success_url=settings.SITE_URL
                + "/?success=true&session_id={CHECKOUT_SESSION_ID}",
                cancel_url=settings.SITE_URL + "/?canceled=true",
            )
            return redirect(checkout_session.url)

        except:
            return Response(
                {"error": "Somenthing went wrong when creating the checkout session"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
