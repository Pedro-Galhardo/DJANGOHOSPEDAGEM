document.addEventListener("DOMContentLoaded", function() {
    const tableRows = document.querySelectorAll("table tbody tr");
    const alterarNomeInput = document.getElementById("alterar_nome");
    const alterarEmailInput = document.getElementById("alterar_email");
    const alterarIdadeInput = document.getElementById("alterar_idade");
    const alterarTelefoneInput = document.getElementById("alterar_telefone");
    const btnAlterar = document.getElementById("btnAlterar");
    const btnExcluir = document.getElementById("btnExcluir");

    let selectedRow = null;
    let selectedRowId = null;

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== "") {
            const cookies = document.cookie.split(";");
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + "=")) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    tableRows.forEach(row => {
        row.addEventListener("click", function() {
            if (selectedRow) {
                selectedRow.classList.remove("selected");
            }

            this.classList.add("selected");
            selectedRow = this;
            selectedRowId = this.dataset.id;

            alterarNomeInput.value = this.dataset.nome || "";
            alterarEmailInput.value = this.dataset.email || "";

            alterarIdadeInput.value = this.dataset.idade && !isNaN(this.dataset.idade) ? this.dataset.idade : "";
            alterarTelefoneInput.value = this.dataset.telefone || "";
        });
    });


    document.addEventListener("click", function(event) {
        if (!event.target.closest("table tbody tr") &&
            !event.target.closest(".action-section")) {

            if (selectedRow) {
                selectedRow.classList.remove("selected");
                selectedRow = null;
                selectedRowId = null;

                alterarNomeInput.value = "";
                alterarEmailInput.value = "";
                alterarIdadeInput.value = "";
                alterarTelefoneInput.value = "";
            }
        }
    });

    btnExcluir.addEventListener("click", function() {
        if (selectedRowId) {
            if (confirm("Tem certeza que deseja excluir este paciente?")) {
                fetch(`/sistema-restrito-crud/delete/${selectedRowId}/`, {
                    method: "POST",
                    headers: {
                        "X-CSRFToken": getCookie("csrftoken"),
                        "Content-Type": "application/json"
                    },
                })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        alert("Paciente excluído com sucesso!");
                        location.reload();
                    } else {
                        alert("Erro ao excluir paciente: " + data.error);
                    }
                })
                .catch(error => {
                    console.error("Erro na requisição de exclusão:", error);
                    alert("Ocorreu um erro ao tentar excluir o paciente.");
                });
            }
        } else {
            alert("Por favor, selecione um paciente para excluir.");
        }
    });

    btnAlterar.addEventListener("click", function() {
        if (selectedRowId) {
            const nome = alterarNomeInput.value;
            const email = alterarEmailInput.value;
            const idade = alterarIdadeInput.value;
            const telefone = alterarTelefoneInput.value;

            const formData = new FormData();
            formData.append("nome", nome);
            formData.append("email", email);
            formData.append("idade", idade);
            formData.append("telefone", telefone);

            fetch(`/sistema-restrito-crud/update/${selectedRowId}/`, {
                method: "POST",
                headers: {
                    "X-CSRFToken": getCookie("csrftoken"),
                },
                body: formData,
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert("Paciente alterado com sucesso!");
                    location.reload();
                } else {
                    alert("Erro ao alterar paciente: " + data.error);
                }
            })
            .catch(error => {
                console.error("Erro na requisição de alteração:", error);
                alert("Ocorreu um erro ao tentar alterar o paciente.");
            });
        } else {
            alert("Por favor, selecione um paciente para alterar.");
        }
    });
    btnGerarRelatorio.addEventListener("click", function() {
        fetch(gerarRelatorioURL)
            .then(response => {
                if (response.ok) {
                    return response.blob();
                } else {
                    return response.json().then(errorData => {
                        throw new Error(errorData.error || "Erro desconhecido ao gerar relatório.");
                    });
                }
            })
            .then(blob => {
                const url = window.URL.createObjectURL(blob);
                const a = document.createElement("a");
                a.style.display = "none";
                a.href = url;
                a.download = "relatorio_historico_pacientes.pdf";
                document.body.appendChild(a);
                a.click();
                window.URL.revokeObjectURL(url);
                alert("Relatório gerado com sucesso!");
            })
            .catch(error => {
                console.error("Erro na requisição do relatório:", error);
                alert("Ocorreu um erro ao tentar gerar o relatório: " + error.message);
            });
    });
});

