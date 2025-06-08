function resetForm() {
            document.getElementById('paciente-form').reset();
            document.getElementById('id').value = '';
        }

        document.getElementById('paciente-form').addEventListener('submit', function (e) {
            e.preventDefault();
            let form = new FormData(this);
            let action = form.get('id') ? 'update' : 'create';
            form.append('action', action);

            fetch('', {
                method: 'POST',
                headers: { 'X-CSRFToken': '{{ csrf_token }}' },
                body: form
            }).then(res => res.json()).then(data => {
                if (data.success) location.reload();
                else alert("Erro ao salvar.");
            });
        });

        function editarPaciente(id, nome, email, idade, telefone) {
            document.getElementById('id').value = id;
            document.getElementById('nome').value = nome;
            document.getElementById('email').value = email;
            document.getElementById('idade').value = idade;
            document.getElementById('telefone').value = telefone;
        }

        function deletarPaciente(id) {
            if (!confirm("Deseja excluir este paciente?")) return;
            let form = new FormData();
            form.append('action', 'delete');
            form.append('id', id);

            fetch('', {
                method: 'POST',
                headers: { 'X-CSRFToken': '{{ csrf_token }}' },
                body: form
            }).then(res => res.json()).then(data => {
                if (data.success) location.reload();
                else alert("Erro ao excluir.");
            });
        }