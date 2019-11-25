from django.db.models.signals import m2m_changed
from django.contrib.auth.models import Group
from django.dispatch import receiver

from evalhubapp.models import User, Evaluator, DaycareUser


@receiver(m2m_changed)
def update_profile_models(instance, action, reverse, model, pk_set, using, *args, **kwargs):
    if model == Group and not reverse:
        evaluator_pk = Group.objects.get(name='evaluator').pk
        daycare_user_pk = Group.objects.get(name='daycare_user').pk

        if action == 'post_add':
            if evaluator_pk in pk_set:
                evaluator = Evaluator(user=instance)
                evaluator.save()
            if daycare_user_pk in pk_set:
                daycare_user = DaycareUser(user=instance, org_name=instance.username)
                daycare_user.save()
