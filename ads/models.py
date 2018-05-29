from django.db import models


class Ad(models.Model):

    BUY = 'BUY'
    SELL = 'SEL'
    TYPES = (
        (BUY, 'Buying'),
        (SELL, 'Selling')
    )

    PENDING = 'PEN'
    APPROVED = 'APR'
    FINISHED = 'FIN'
    STATUSES = (
        (PENDING, 'Pending'),
        (APPROVED, 'Approved'),
        (FINISHED, 'Finished')
    )

    name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)  # null=True, blank=True => campo opcional
    price = models.FloatField()
    image = models.FileField(null=True)  # null=True => campo opcional
    send_choice = models.BooleanField(default=False)
    type = models.CharField(max_length=3, choices=TYPES, default=SELL)
    status = models.CharField(max_length=3, choices=STATUSES, default=PENDING)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Define cómo se representa un Ad como una string
        """
        return '{0} ({1} €)'.format(self.name, self.price)
