from django.shortcuts import render
from .models import FispTransaction
from account.models import AgentProfile
from account.serializers import FispTransactionSerializer
from rest_framework import viewsets
from django.views.generic import ListView
from django_filters.views import FilterView
from datetime import datetime, timedelta
from django.shortcuts import get_object_or_404

# Create your views here.
class FispTransactionViewSet(viewsets.ModelViewSet):
    queryset = FispTransaction.objects.all()
    serializer_class = FispTransactionSerializer


class TransactionListView(ListView):
    model = FispTransaction
    template_name = 'admin/transaction_list.html'
    context_object_name = 'transactions'
    
    def get_queryset(self):
        user_account_type = self.request.user.account_type
        transactions = []
        
        if user_account_type:
            for agent in user_account_type.agents_to_manage.all():
                agent_id = agent.id
                print('my txn ',agent_id,FispTransaction.objects.filter(agent=agent))
                return FispTransaction.objects.filter()

                # is_success = True
                # end_date = datetime.now()
                # start_date = end_date - timedelta(days=7)

                # agent_transactions = FispTransaction.objects.filter(
                #     agent=agent_instance,
                #     isSuccess=is_success,
                #     timestamp__range=(start_date, end_date)
                # )
                # transactions.extend(agent_transactions)

                # return transactions 
    
    
    def get(self, request, *args, **kwargs):
        transactions = self.get_queryset()
        return render(request, self.template_name, {'transactions': transactions})
    