const ctx = document.getElementById('myChart');
          new Chart(ctx, {
            type: 'bar',
            data: {
              labels: [
                {% for item in labels %}
                "{{ item }}",
                {% endfor %}
              ],
              datasets: [{
                label: '# of Votes',
                data: [
                  {% for item in values %}
                 "{{ item }}",
                 {% endfor %}
                ],
                borderWidth: 1
              }]
            },
            options: {
              scales: {
                y: {
                  beginAtZero: true
                }
              }
            }
          });