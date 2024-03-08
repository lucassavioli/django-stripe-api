import { useEffect, useState } from "react";
import { API_URL } from "../config";
import { useLocation } from "react-router-dom";
import QueryString from "query-string";

export default function HomePage() {
  const [message, setMessage] = useState("");
  const location = useLocation();

  useEffect(() => {
    // Check to see if this is a redirect back from Checkout
    const values = QueryString.parse(location.search);
    console.log(values);
    
    
    if (values.success) {
      setMessage("Order placed! You will receive an email confirmation.");
    }

    if (values.canceled) {
      setMessage(
        "Order canceled -- continue to shop around and checkout when you're ready."
      );
    }
  }, []);
  return (
    <section>
      <div className="product">
        <img width={300}
          src="https://m.media-amazon.com/images/I/71e7d0OWhvL._AC_UF1000,1000_QL80_.jpg"
          alt="The cover of Stubborn Attachments"
        />
        <div className="description">
          <h3>Book 12 rules for life - Jordan Peterson</h3>
          <h5>$20.00</h5>
        </div>
      </div>
      <form
        action={`${API_URL}/api/stripe/create-checkout-session`}
        method="POST"
      >
        <button className="button" type="submit">Checkout</button>
      </form>
    </section>
  );
}
