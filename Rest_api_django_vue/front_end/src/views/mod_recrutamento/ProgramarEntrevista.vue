<script setup>
import { FilterMatchMode } from 'primevue/api';
import { ref, onMounted, onBeforeMount } from 'vue';
import { ProductService } from '@/service/ProductService';
import { useToast } from 'primevue/usetoast';
import '@/assets/mod_recrutamento/programarEntrevista.scss';

const toast = useToast();
const products = ref(null); 
const productDialog = ref(false);
const deleteProductDialog = ref(false);
const deleteProductsDialog = ref(false);
const product = ref({});
const selectedProducts = ref(null);
const dt = ref(null);
const filters = ref({});
const submitted = ref(false);
const productService = new ProductService(); 
const breadcrumbHome = ref({ icon: 'pi pi-home', to: '/' });
const breadcrumbItems = ref([{ label: 'Recrutamento e Selecção' }, { label: 'Programar Entrevista' }]);


onBeforeMount(() => {
    initFilters();
});
onMounted(() => {
    productService.getProducts().then((data) => (products.value = data));
});
const formatCurrency = (value) => {
    return value.toLocaleString('en-US', { style: 'currency', currency: 'AKZ' });
};

const openNew = () => {
    product.value = {};
    submitted.value = false;
    productDialog.value = true;
};

const hideDialog = () => {
    productDialog.value = false;
    submitted.value = false;
};


const findIndexById = (id) => {
    let index = -1;
    for (let i = 0; i < products.value.length; i++) {
        if (products.value[i].id === id) {
            index = i;
            break;
        }
    }
    return index;
};

const createId = () => {
    let id = '';
    const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    for (let i = 0; i < 5; i++) {
        id += chars.charAt(Math.floor(Math.random() * chars.length));
    }
    return id;
};

const exportCSV = () => {
    dt.value.exportCSV();    
};

const confirmDeleteSelected = () => {
    deleteProductsDialog.value = true;
};
const deleteSelectedProducts = () => {
    products.value = products.value.filter((val) => !selectedProducts.value.includes(val));
    deleteProductsDialog.value = false;
    selectedProducts.value = null;
    toast.add({ severity: 'success', summary: 'Successo', detail: 'Apagado', life: 100 });
};

const initFilters = () => {
    filters.value = {
        global: { value: null, matchMode: FilterMatchMode.CONTAINS }
    };
};

const visibleNovaCampanha = ref(false);
const visibleVisualizarCampanha = ref(false);

const dropdownItems = ref([
    { name: 'Option 1', code: 'Option 1' },
    { name: 'Option 2', code: 'Option 2' },
    { name: 'Option 3', code: 'Option 3' }
]);

const dropdownItem = ref(null);

const buttondisplay = ref();
const icondisplay = ref();
const templatedisplay = ref();

</script>

<template>
    <div class="grid">
        <div class="col-12 lg:col-2 xl:col-12">
            <Breadcrumb :home="breadcrumbHome" :model="breadcrumbItems" id="breadcrumb" />
        </div>
        <div class="col-12">
            <div class="card" id="cart">
                <Toolbar class="mb-4" style="border: none;">
                    <template v-slot:start>
                        <div class="my-2">
                         
                        </div>
                    </template>

                    <template v-slot:end>
                        <Button label="Novo" icon="pi pi-plus" class="mr-2" severity="success" @click="visibleNovaCampanha = true" />
                        <Button style="background-color:#0077B6;" label="Exportar" icon="pi pi-upload" severity="help" @click="exportCSV($event)" />
                    </template>
                </Toolbar>

                <DataTable
                    ref="dt"
                    :value="products"
                    v-model:selection="selectedProducts"
                    dataKey="id"
                    :paginator="true"
                    :rows="5"
                    :filters="filters"
                    paginatorTemplate="FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink CurrentPageReport RowsPerPageDropdown"
                    :rowsPerPageOptions="[5, 10, 25]"
                    currentPageReportTemplate="Showing {first} to {last} of {totalRecords} products"
                >
                    <template #header>
                        <div class="flex flex-column md:flex-row md:justify-content-between md:align-items-center">
                            <h5 class="m-0"></h5>
                            <IconField iconPosition="left" class="block mt-2 md:mt-0">
                                <InputIcon class="pi pi-search" />
                                <InputText class="w-full sm:w-auto" v-model="filters['global'].value" placeholder="Pesquisar..." />
                            </IconField>
                        </div>
                    </template>

                    <Column selectionMode="multiple" headerStyle="width:3rem"></Column>
                    <Column field="code" header="Referência" :sortable="true"></Column>
                    <Column field="name" header="Nome" :sortable="true"></Column>
                    <Column field="name" header="Tempo" :sortable="true"> </Column>
                    <Column field="name" header="Data" :sortable="true"> </Column>
                    <Column field="name" header="Campanha" :sortable="true"> </Column>
                    <Column field="name" header="Candidato" :sortable="true"> </Column>
                    <Column field="name" header="Entrevistador" :sortable="true"> </Column>
                    <Column field="name" header="Dt. Adic" :sortable="true"> </Column>
                    <Column field="name" header="Adicionado" :sortable="true"> </Column>
                    <Column field="name" header="Status" :sortable="true"> </Column>
                    <Column headerStyle="width:20%; min-width:5%;">
                        <template #body="slotProps">
                            <Button icon="pi pi-eye" class="mt-2" severity="success" rounded  @click="visibleVisualizarCampanha = true" />
                            <Button icon="pi pi-pencil" class="mr-2" severity="success" rounded @click="" />
                            <Button icon="pi pi-trash" class="mt-2" severity="success" rounded @click="" />
                            
                        </template>
                    </Column>
                </DataTable>
                <Sidebar v-model:visible="visibleNovaCampanha" header="Nova Entrevista" position="right" id="side_bar">

                    <img src="/layout/images/login/logo.png" alt="Image" height="100" class="mb-3" />
 
                    <div class="col-12">
                        <div class="p-fluid formgrid grid">
                            <div class="field col-12">
                                <label>Imformações Gerais:</label>
                            </div>
                            <div class="field col-4">
                                <Dropdown id="state" v-model="dropdownItem" :options="dropdownItems" optionLabel="name" placeholder="Campanha de Recrutamento"></Dropdown>
                            </div>
                            <div class="field col-4">
                                <Dropdown id="state" v-model="dropdownItem" :options="dropdownItems" optionLabel="name" placeholder="Posição"></Dropdown>
                            </div>
                            <div class="field col-4">
                                <Calendar v-model="icondisplay" showIcon iconDisplay="input" inputId="icondisplay" />
                            </div>
                            <div class="field col-12">
                                <InputText placeholder="Nome do Cr. Campanha" id="" type="text" />
                            </div>
                            <div class="field col-12">
                                <Dropdown id="state" v-model="dropdownItem" :options="dropdownItems" optionLabel="name" placeholder="Entrevistador"></Dropdown>
                            </div>
                            <div class="field col-4">
                                <label>De: (Hora)</label>
                                <Calendar v-model="templatedisplay" showIcon iconDisplay="input" timeOnly inputId="templatedisplay">
                                    <template #inputicon="{ clickCallback }">
                                        <InputIcon class="pi pi-clock cursor-pointer" @click="clickCallback" />
                                    </template>
                                </Calendar>
                            </div>
                            <div class="field col-4">
                                <label>Para: (Hora)</label>
                                <Calendar v-model="templatedisplay" showIcon iconDisplay="input" timeOnly inputId="templatedisplay">
                                    <template #inputicon="{ clickCallback }">
                                        <InputIcon class="pi pi-clock cursor-pointer" @click="clickCallback" />
                                    </template>
                                </Calendar>
                            </div>
                            <div class="field col-4"> </div>
                            <div class="field col-12">
                                <label>Candidatos:</label>
                            </div>
                            <div class="field col-4">
                                <Dropdown id="state" v-model="dropdownItem" :options="dropdownItems" optionLabel="name" placeholder="Candidatos"></Dropdown>
                            </div>
                            <div class="field col-4">
                                <InputText placeholder="email" id="" type="email" />
                            </div>
                            <div class="field col-4">
                                <InputText placeholder="Telefone" id="" type="number" />
                            </div>

                            <div class="field col-6">
                            </div>
                            <div class="field col-6">
                                <Button style="width:100%" label="Salvar" icon="pi pi-plus" class="mr-2" severity="success" @click="" />   
                            </div>                            
                        </div>
                    </div>
                

                </Sidebar>

                <Sidebar v-model:visible="visibleVisualizarCampanha" header="Visualizar Campanha" position="right" id="side_bar">
                    <img src="/layout/images/login/logo.png" alt="Image" height="100" class="mb-3" />

                    <div class="col-12">
                        <div class="p-fluid formgrid grid">
                            <div class="field col-12"> <label id="cabecalho">Dados da Entrevista:</label> </div>
                            <div class="field col-3"> <label class="ref">Campanha de Recrutamento:</label> </div>
                            <div class="field col-9" id="cart_view"> <label class="desc">jkgfvklv</label> </div>
                            <div class="field col-3" > <label class="ref">Nome do cronograma de entrevista:</label> </div>
                            <div class="field col-9" id="cart_view"> <label class="desc">jkgfvklv</label> </div>
                            <div class="field col-3" > <label class="ref">Data da entrevista:</label> </div>
                            <div class="field col-9" id="cart_view"> <label class="desc">jkgfvklv</label> </div>
                            <div class="field col-3" > <label class="ref">De (hora):</label> </div>
                            <div class="field col-9" id="cart_view"> <label class="desc">jkgfvklv</label> </div>
                            <div class="field col-3" > <label class="ref">Para (hora):</label> </div>
                            <div class="field col-9" id="cart_view"> <label class="desc">jkgfvklv</label> </div>
                            <div class="field col-3" > <label class="ref">Entrevistador:</label> </div>
                            <div class="field col-9" id="cart_view"> <label class="desc">jkgfvklv</label> </div>
                            <br>
                            <div class="field col-3" > <label class="ref">Candidato:</label> </div>
                            <div class="field col-9" id="cart_view"> <label class="desc">jkgfvklv</label> </div>
                            <div class="field col-3" > <label class="ref">Email:</label> </div>
                            <div class="field col-9" id="cart_view"> <label class="desc">jkgfvklv</label> </div>
                            <div class="field col-3" > <label class="ref">Numero de Telefone:</label> </div>
                            <div class="field col-9" id="cart_view"> <label class="desc">jkgfvklv</label> </div>
                        </div>
                    </div>

                </Sidebar>


                <Dialog v-model:visible="deleteProductDialog" :style="{ width: '450px' }" header="Confirm" :modal="true">
                    <div class="flex align-items-center justify-content-center">
                        <i class="pi pi-exclamation-triangle mr-3" style="font-size: 2rem" />
                        <span v-if="product">Tens certeza que queres eliminar este Item?</span>
                    </div>
                    <template #footer>
                        <Button label="No" icon="pi pi-times" text @click="deleteProductDialog = false" />
                        <Button label="Yes" icon="pi pi-check" text @click="deleteProduct" />
                    </template>
                </Dialog>

                <Dialog v-model:visible="deleteProductsDialog" :style="{ width: '450px' }" header="Confirm" :modal="true">
                    <div class="flex align-items-center justify-content-center">
                        <i class="pi pi-exclamation-triangle mr-3" style="font-size: 2rem" />
                        <span v-if="product">Tens certeza que queres eliminar este Item?</span>
                    </div>
                    <template #footer>
                        <Button label="No" icon="pi pi-times" text @click="deleteProductsDialog = false" />
                        <Button label="Yes" icon="pi pi-check" text @click="deleteSelectedProducts" />
                    </template>
                </Dialog>
            </div>
        </div>
    </div>
</template>
