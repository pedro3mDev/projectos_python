<script setup>
import { onMounted, reactive, ref, watch } from 'vue';
import { ProductService } from '@/service/ProductService';
import { useLayout } from '@/layout/composables/layout';
import '@/assets/ajuda.scss';

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


const sobre_sistema = ref(false);
const recrutamento = ref(false);
const gest_intg = ref(false);
const td = ref(false);
const gest_des_indiv = ref(false);
const gest_lideranca = ref(false);
const gest_remunerac = ref(false);
const gest_doc = ref(false);
const gest_ferias = ref(false);
const prod_relat = ref(false);
const plan_forc_trab = ref(false);
const eng_talentos = ref(false);
const gest_viagens = ref(false);
const gest_form = ref(false);


const breadcrumbHome = ref({ icon: 'pi pi-home', to: '/' });
const breadcrumbItems = ref([{ label: 'Home' }, { label: 'Ajuda' }]);

</script>

<template>
    <div class="grid">
        <div class="col-12 lg:col-2 xl:col-12">
            <Breadcrumb :home="breadcrumbHome" :model="breadcrumbItems" id="breadcrumb" />
        </div>

        <div class="col-12 lg:col-6 xl:col-3">
            <div class="card mb-0" id="cart">
                <div class="col-12" id="cartoes_perfil">
                    <div class="text-900 font-small"> 
                        <Button icon="pi pi-arrow-left" @click="sobre_sistema = true" class="cartoes_perfil_btn"> 
                            Sobre o Sistema
                        </Button>
                        <Button label="" icon=" pi pi-arrow-right" iconPos="right" id="avancar" /> 
                    </div>  
                    <Sidebar v-model:visible="sobre_sistema" header="Right Sidebar" position="right" id="side_bar">
                        
                    </Sidebar>
                </div>
            </div>
        </div>

        <div class="col-12 lg:col-6 xl:col-3">
            <div class="card mb-0" id="cart">
                <div class="col-12" id="cartoes_perfil">
                    <div class="text-900 font-small"> 
                        <Button icon="pi pi-arrow-left" @click="recrutamento = true" class="cartoes_perfil_btn"> 
                            Recrutamento e Selecção
                        </Button>
                        <Button label="" icon=" pi pi-arrow-right" iconPos="right" @click="recrutamento = true" id="avancar" />
                    </div>  
                    <Sidebar v-model:visible="recrutamento" header="Right Sidebar" position="right" id="side_bar">
                        
                    </Sidebar>
                </div>
            </div>
        </div>

        <div class="col-12 lg:col-6 xl:col-3">
            <div class="card mb-0" id="cart">
                <div class="col-12" id="cartoes_perfil">
                    <div class="text-900 font-small"> 
                        <Button icon="pi pi-arrow-left" @click="gest_intg = true" class="cartoes_perfil_btn"> 
                            Gestão da Integração
                        </Button>
                        <Button label="" @click="gest_intg = true" icon=" pi pi-arrow-right" iconPos="right" id="avancar" />
                    </div>  
                    <Sidebar v-model:visible="gest_intg" header="Right Sidebar" position="right" id="side_bar">
                        
                    </Sidebar>
                </div>
            </div>
        </div>

        <div class="col-12 lg:col-6 xl:col-3">
            <div class="card mb-0" id="cart">
                <div class="col-12" id="cartoes_perfil">
                    <div class="text-900 font-small"> 
                        <Button icon="pi pi-arrow-left" @click="td = true" class="cartoes_perfil_btn"> 
                            TD - Políticas da Empresa
                        </Button>
                        <Button label="" icon=" pi pi-arrow-right" @click="td = true" iconPos="right" id="avancar" />
                    </div>  
                    <Sidebar v-model:visible="td" header="Right Sidebar" position="right" id="side_bar">
                        
                    </Sidebar>
                </div>
            </div>
        </div>

        <div class="col-12 lg:col-6 xl:col-3">
            <div class="card mb-0" id="cart">
                <div class="col-12" id="cartoes_perfil">
                    <div class="text-900 font-small"> 
                        <Button icon="pi pi-arrow-left" @click="gest_des_indiv = true" class="cartoes_perfil_btn"> 
                            Gestão do Desenvolvimento Individual
                        </Button>
                        <Button label="" icon=" pi pi-arrow-right" @click="gest_des_indiv = true" iconPos="right" id="avancar" />
                    </div>  
                    <Sidebar v-model:visible="gest_des_indiv" header="Right Sidebar" position="right" id="side_bar">
                        
                    </Sidebar>
                </div>
            </div>
        </div>

        <div class="col-12 lg:col-6 xl:col-3">
            <div class="card mb-0" id="cart">
                <div class="col-12" id="cartoes_perfil">
                    <div class="text-900 font-small"> 
                        <Button icon="pi pi-arrow-left" @click="gest_lideranca = true" class="cartoes_perfil_btn"> 
                            Gestão de Plano de Sucessão e Liderança
                        </Button>
                        <Button label="" icon=" pi pi-arrow-right" @click="gest_lideranca = true" iconPos="right" id="avancar" />
                    </div>  
                    <Sidebar v-model:visible="gest_lideranca" header="Right Sidebar" position="right" id="side_bar">
                        
                    </Sidebar>
                </div>
            </div>
        </div>

        <div class="col-12 lg:col-6 xl:col-3">
            <div class="card mb-0" id="cart">
                <div class="col-12" id="cartoes_perfil">
                    <div class="text-900 font-small"> 
                        <Button icon="pi pi-arrow-left" @click="gest_remunerac = true" class="cartoes_perfil_btn"> 
                            Gestão de Remunerações
                        </Button>
                        <Button label="" @click="gest_remunerac = true" icon=" pi pi-arrow-right" iconPos="right" id="avancar" />
                    </div>  
                    <Sidebar v-model:visible="gest_remunerac" header="Right Sidebar" position="right" id="side_bar">
                        
                    </Sidebar>
                </div>
            </div>
        </div>

        <div class="col-12 lg:col-6 xl:col-3">
            <div class="card mb-0" id="cart">
                <div class="col-12" id="cartoes_perfil">
                    <div class="text-900 font-small"> 
                        <Button icon="pi pi-arrow-left" @click="gest_doc = true" class="cartoes_perfil_btn"> 
                            Gestão Documental
                        </Button>
                        <Button label="" icon=" pi pi-arrow-right" @click="gest_doc = true" iconPos="right" id="avancar" />
                    </div>  
                    <Sidebar v-model:visible="gest_doc" header="Right Sidebar" position="right" id="side_bar">
                        
                    </Sidebar>
                </div>
            </div>
        </div>

        <div class="col-12 lg:col-6 xl:col-3">
            <div class="card mb-0" id="cart">
                <div class="col-12" id="cartoes_perfil">
                    <div class="text-900 font-small"> 
                        <Button icon="pi pi-arrow-left" @click="gest_ferias = true" class="cartoes_perfil_btn"> 
                            Gestão de Assiduidade e Férias
                        </Button>
                        <Button label="" icon=" pi pi-arrow-right" @click="gest_ferias = true" iconPos="right" id="avancar" />
                    </div>  
                    <Sidebar v-model:visible="gest_ferias" header="Right Sidebar" position="right" id="side_bar">

                    </Sidebar>
                </div>
            </div>
        </div>

        <div class="col-12 lg:col-6 xl:col-3">
            <div class="card mb-0" id="cart">
                <div class="col-12" id="cartoes_perfil">
                    <div class="text-900 font-small"> 
                        <Button icon="pi pi-arrow-left" @click="prod_relat = true" class="cartoes_perfil_btn"> 
                            Produção de Relatórios e Dashboard
                        </Button>
                        <Button label="" icon=" pi pi-arrow-right" iconPos="right" @click="prod_relat = true" id="avancar" />
                    </div>  
                    <Sidebar v-model:visible="prod_relat" header="Right Sidebar" position="right" id="side_bar">
                        
                    </Sidebar>
                </div>
            </div>
        </div>

        <div class="col-12 lg:col-6 xl:col-3">
            <div class="card mb-0" id="cart">
                <div class="col-12" id="cartoes_perfil">
                    <div class="text-900 font-small"> 
                        <Button icon="pi pi-arrow-left" @click="plan_forc_trab = true" class="cartoes_perfil_btn"> 
                            Planeamento de Força de Trabalho
                        </Button>
                        <Button label="" icon=" pi pi-arrow-right" @click="plan_forc_trab = true" iconPos="right" id="avancar" />
                    </div>  
                    <Sidebar v-model:visible="plan_forc_trab" header="Right Sidebar" position="right" id="side_bar">
                        
                    </Sidebar>
                </div>
            </div>
        </div>

        <div class="col-12 lg:col-6 xl:col-3">
            <div class="card mb-0" id="cart">
                <div class="col-12" id="cartoes_perfil">
                    <div class="text-900 font-small"> 
                        <Button icon="pi pi-arrow-left" @click="eng_talentos = true" class="cartoes_perfil_btn"> 
                            Engajamento de Talentos
                        </Button>
                        <Button label="" icon=" pi pi-arrow-right" @click="eng_talentos = true" iconPos="right" id="avancar" />
                    </div>  
                    <Sidebar v-model:visible="eng_talentos" header="Right Sidebar" position="right" id="side_bar">
                         
                    </Sidebar>
                </div>
            </div>
        </div>

        <div class="col-12 lg:col-6 xl:col-3">
            <div class="card mb-0" id="cart">
                <div class="col-12" id="cartoes_perfil">
                    <div class="text-900 font-small"> 
                        <Button icon="pi pi-arrow-left" @click="gest_viagens = true" class="cartoes_perfil_btn"> 
                            Gestão de Viagem
                        </Button>
                        <Button label="" icon=" pi pi-arrow-right" @click="gest_viagens = true" iconPos="right" id="avancar" />
                    </div>  
                    <Sidebar v-model:visible="gest_viagens" header="Right Sidebar" position="right" id="side_bar">
                        
                    </Sidebar>
                </div>
            </div>
        </div>

        <div class="col-12 lg:col-6 xl:col-3">
            <div class="card mb-0" id="cart">
                <div class="col-12" id="cartoes_perfil">
                    <div class="text-900 font-small"> 
                        <Button icon="pi pi-arrow-left" @click="gest_form = true" class="cartoes_perfil_btn"> 
                            Gestão da Formação
                        </Button>
                        <Button label="" @click="gest_form = true" icon=" pi pi-arrow-right" iconPos="right" id="avancar" />
                    </div>  
                    <Sidebar v-model:visible="gest_form" header="Right Sidebar" position="right" id="side_bar">
                        
                    </Sidebar>
                </div>
            </div>
        </div>
    </div>
</template>



