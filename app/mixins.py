from django.contrib.contenttypes.models import ContentType
from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import TemplateView, View
from abc import ABC, abstractmethod

from app.helpers import data_handler
from app.models import Comments
from users.models import CustomUser


class RenderOrRedirect(ABC, TemplateView):
    trigger = "next"

    @property
    @abstractmethod
    def redirect_to(self):
        pass

    def get(self, request, *args, **kwargs):
        if self.trigger in request.GET:
            return redirect(self.redirect_to)

        return render(request, self.template_name)


class CommentsHandlerMixin(ABC, View):

    @abstractmethod
    def get_model_class(self):
        """
        Must be implemented to return the model class (Thread or Publications).
        """
        pass

    def get_context_data(self, request, **kwargs):
        pk = self.kwargs.get("pk")
        get_data = data_handler(request, pk)
        user_id = get_data["user_id"]
        model_class = self.get_model_class()
        instance = get_object_or_404(model_class, pk=pk)

        context = {"user_id": user_id, "instance": instance, "pk": pk}
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(request, **kwargs)
        instance = context["instance"]

        if instance:
            content = request.POST.get("feedback")
            try:
                user = CustomUser.objects.get(id=context["user_id"])
                content_type = ContentType.objects.get_for_model(instance.__class__)
                Comments.objects.create(
                    user=user,
                    title=instance.title,
                    context=content,
                    content_type=content_type,
                    object_id=context.get("pk"),
                )
                return JsonResponse(data_handler(request, context["pk"]))
            except CustomUser.DoesNotExist:
                return JsonResponse({"message": "User not found"}, status=404)
            except Exception as e:
                return JsonResponse({"message": str(e)}, status=500)

        return JsonResponse({"message": "Invalid request"}, status=400)


class RemoveCommentsMixin(ABC, View):
    def remove_comment(self, request, *args, **kwargs):
        answer_id = self.kwargs.get("answer_id")
        try:
            answer = Comments.objects.get(id=answer_id)
            answer.delete()
            return HttpResponse(status=204)
        except Comments.DoesNotExist:
            return JsonResponse({"error": "Comments does not exist"}, status=404)