<script setup>
import { onMounted, reactive, ref, watch } from 'vue';
import { ProductService } from '@/service/ProductService';
import { useLayout } from '@/layout/composables/layout';
import '@/assets/perfil.scss';

const { isDarkTheme } = useLayout();
const products = ref(null);
const lineOptions = ref(null);
const productService = new ProductService();
const applyLightTheme = () => {
    lineOptions.value = {
        plugins: {
            legend: {
                labels: {
                    color: '#495057'
                }
            }
        },
        scales: {
            x: {
                ticks: {
                    color: '#495057'
                },
                grid: {
                    color: '#ebedef'
                }
            },
            y: {
                ticks: {
                    color: '#495057'
                },
                grid: {
                    color: '#ebedef'
                }
            }
        }
    };
};
const applyDarkTheme = () => {
    lineOptions.value = {
        plugins: {
            legend: {
                labels: {
                    color: '#ebedef'
                }
            }
        },
        scales: {
            x: {
                ticks: {
                    color: '#ebedef'
                },
                grid: {
                    color: 'rgba(160, 167, 181, .3)'
                }
            },
            y: {
                ticks: {
                    color: '#ebedef'
                },
                grid: {
                    color: 'rgba(160, 167, 181, .3)'
                }
            }
        }
    };
};

watch(
    isDarkTheme,
    (val) => {
        if (val) {
            applyDarkTheme();
        } else {
            applyLightTheme();
        }
    },
    { immediate: true }
);


const visibleRight = ref(false);
const breadcrumbHome = ref({ icon: 'pi pi-home', to: '/' });
const breadcrumbItems = ref([{ label: 'Home' }, { label: 'User/Perfil' }]);

</script>

<template>
    <div class="grid">
        <div class="col-12 lg:col-2 xl:col-12">
            <Breadcrumb :home="breadcrumbHome" :model="breadcrumbItems" id="breadcrumb" />
        </div>

        <div class="col-12 lg:col-6 xl:col-12">
            <div class="card mb-0" id="cart_titulo">
                <div>
                    <div id="titulo" class="text-900 font-medium text-xl card mb-20">
                        <!--Avatar image="https://www.gravatar.com/avatar/05dfd4b41340d09cae045235eb0893c3?d=mp" class="mr-2" size="xlarge" shape="circle" /-->
                        <img src="/layout/images/login/logo.png" alt="Image" height="50" class="mb-3" />
                        Felipe da Costa
                    </div>
                </div>
            </div>
            
        </div>

        <div class="col-12 lg:col-6 xl:col-3">
            <div class="card mb-0" id="cart_titulo">
                <div class="text-900 font-medium text-xl" style="margin-bottom:10px;">
                    Sumário
                </div>
                <div class="col-12" id="titulo">
                    <div class="text-900 font-small"> 
                        <Badge value="7"></Badge> 
                        Itens Assinados por Mim
                    </div>
                </div>
                <div class="col-12" id="titulo">
                    <div class="text-900 font-small"> 
                        <Badge value="7"></Badge> 
                        Questionários Assinados por Mim
                    </div>
                </div>

                <div class="col-12" id="titulo">
                    <div class="text-900 font-small"> 
                        <i class="pi pi-folder-plus" style="font-size: 2rem"></i>
                        Estrutrura de Pastas
                    </div>
                </div>
            </div>
        </div>

        <div class="col-12 lg:col-6 xl:col-6">
            <div class="card mb-0" id="cart_titulo">
                <div class="text-900 font-medium text-xl" style="margin-bottom:10px;">
                    Minha Carreira
                </div>

                <div class="col-12" id="titulo">
                    <div class="text-900 font-small"> 
                        Certificados
                    </div>
                </div>
                <div class="col-12" id="titulo">
                    <div class="text-900 font-small"> 
                        Performance Goals
                    </div>
                </div>
                <div class="col-12" id="titulo">
                    <div class="text-900 font-small" style="padding:10px;"> 
                        Dados Pessoais 
                        <!--div class="card" style="border-radius:0px; border:none;>
                            <TreeTable :value="nodes">
                                <Column field="name" header="" expander></Column>
                                <Column field="size" header=""></Column>
                                <Column field="type" header=""></Column>
                            </TreeTable>
                        </div-->

                    </div>
                </div>
            </div>
        </div>

        <div class="col-12 lg:col-6 xl:col-3">
            <div class="card mb-0" id="cart_titulo">
                <div class="text-900 font-medium text-xl" style="margin-bottom:10px;">
                    Informação Adicional
                </div>
                
                <div class="col-12" id="titulo">
                    <div class="text-900 font-small">Beneficios</div>
                    <p></p>
                </div>
                <div class="col-12" id="titulo">
                    <div class="text-900 font-small">Perfonance</div>
                    <p></p>
                </div>
                <div class="col-12" id="titulo">
                    <div class="text-900 font-small">Competencias</div>
                    <p></p>
                </div>
                <div class="col-12" id="titulo">
                    <div class="text-900 font-small">Organização</div>
                    <p></p>
                </div>
                <div class="col-12" id="titulo">
                    <div class="text-900 font-small"> 
                        <Button icon="pi pi-arrow-left" @click="visibleRight = true" class="cartoes_perfil_btn"> 
                            Questionários
                        </Button>
                    </div>  
                    <Sidebar v-model:visible="visibleRight" header="Right Sidebar" position="right">
                        
                    </Sidebar>
                </div>
            </div>
        </div>
    </div>
</template>
