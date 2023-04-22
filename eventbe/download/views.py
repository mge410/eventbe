import io

from django.conf import settings
from django.http import FileResponse
from django.http import HttpRequest
from django.views.generic import View
from reportlab.pdfgen import canvas


class DownloadUserDataView(View):
    def get(self, request: HttpRequest) -> FileResponse:
        buffer = io.BytesIO()
        p = canvas.Canvas(buffer, bottomup=1)
        p.setPageSize((290, 500))
        p.drawImage(
            f'{settings.STATICFILES_DIRS[0]}/img/background_pdf.jpg',
            x=0,
            y=0,
            width=290,
            height=500,
        )
        user = request.user
        if user:
            p.setTitle(f'{user.username}')
            p.drawString(45, 300, f'I am: {user.username}')
            p.drawString(45, 280, f'{user.email}')
            p.drawString(45, 260, f'Balance: {user.coins} coins')
            p.drawString(45, 240, f'Events visited: {user.events_visited}')
            p.drawString(45, 220, f'Events organized: {user.events_organized}')
            p.drawImage(
                f'{settings.STATICFILES_DIRS[0]}/img/fritz-kola.png',
                x=42,
                y=100,
                width=207,
                height=50,
            )
        p.showPage()
        p.save()
        buffer.seek(0)
        return FileResponse(
            buffer,
            as_attachment=True,
            filename='userdata.pdf',
        )
