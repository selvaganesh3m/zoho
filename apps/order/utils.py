from django.core.mail import send_mail
from reportlab.pdfgen import canvas
from io import BytesIO
from django.core.files.base import ContentFile
from .models import ProductionOrder
from django.shortcuts import get_object_or_404


def send_email_to_user(order):
    subject = "Order Ready"
    body = f"Your order {order.id} is now ready for collection."
    from_email = "notify@manufacturinglab.io"
    to_email = ["selvaganesh3m@gmail.com"]
    send_mail(subject, "", from_email, to_email, html_message=body)


def generate_and_save_invoice(order):
    
    buffer = BytesIO()

    p = canvas.Canvas(buffer)

    p.setFont("Helvetica", 20)

    p.drawString(100, 700, f"Invoice Generated for Order {order.id}")

    p.showPage()
    p.save()

    pdf_content = buffer.getvalue()
    buffer.close()

    new_invoice = order
    new_invoice.invoice.save(f"invoice_{order.id}.pdf", ContentFile(pdf_content))

    return new_invoice.invoice.url
