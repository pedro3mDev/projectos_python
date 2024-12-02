<script setup>
import { onMounted, reactive, ref, watch } from 'vue';
import { ProductService } from '@/service/ProductService';
import { useLayout } from '@/layout/composables/layout';
import '@/assets/mod_recrutamento/painel.scss';
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

onMounted(() => {
    chartData.value = setChartData();
    chartOptions.value = setChartOptions();
});

const chartData = ref();
const chartOptions = ref();
const setChartData = () => {
    const documentStyle = getComputedStyle(document.body);
    return {
        labels: ['A', 'B', 'C'],
        datasets: [
            {
                data: [540, 325, 702],
                backgroundColor: [documentStyle.getPropertyValue('--p-cyan-500'), documentStyle.getPropertyValue('--p-orange-500'), documentStyle.getPropertyValue('--p-gray-500')],
                hoverBackgroundColor: [documentStyle.getPropertyValue('--p-cyan-400'), documentStyle.getPropertyValue('--p-orange-400'), documentStyle.getPropertyValue('--p-gray-400')]
            }
        ]
    };
};

const setChartOptions = () => {
    const documentStyle = getComputedStyle(document.documentElement);
    const textColor = documentStyle.getPropertyValue('--p-text-color');
    return {
        plugins: {
            legend: {
                labels: {
                    usePointStyle: true,
                    color: textColor
                }
            }
        }
    };
};
const breadcrumbHome = ref({ icon: 'pi pi-home', to: '/' });
const breadcrumbItems = ref([{ label: 'Recrutamento e Selecção' }, { label: 'Painel' }]);

</script>



<template>
    <div class="grid">
        <div class="col-12 lg:col-2 xl:col-12">
            <Breadcrumb :home="breadcrumbHome" :model="breadcrumbItems" id="breadcrumb" />
        </div>
        <div class="col-12 lg:col-2 xl:col-3">
            <div class="card mb-0" id="cartao">
                <div class="flex justify-content-between mb-3">
                    <div>
                        <span class="block text-500 font-medium mb-3">
                        Campanha total 
                        </span>
                    </div>
                    <div class="flex align-items-center justify-content-center border-round" id="div_icone" >
                        <i class="pi pi-user text-xl" id="icone"></i>
                    </div>
                </div>
            </div>
        </div>
        <div class="col-12 lg:col-2 xl:col-3">
            <div class="card mb-0" id="cartao">
                <div class="flex justify-content-between mb-3">
                    <div>
                        <span class="block text-500 font-medium mb-3">
                            Campanhas em andamento 
                        </span>
                        <div class="text-900 font-medium text-xl"></div>
                    </div>
                    <div class="flex align-items-center justify-content-center border-round" id="div_icone" >
                        <i class="pi pi-user text-xl" id="icone"></i>
                    </div>
                </div>
            </div>
        </div>
        <div class="col-12 lg:col-2 xl:col-3" >
            <div class="card mb-0" id="cartao">
                <div class="flex justify-content-between mb-3">
                    <div>
                        <span class="block text-500 font-medium mb-3">
                            Campanhas planejadas 
                        </span>
                        <div class="text-900 font-medium text-xl"></div>
                    </div>
                    <div class="flex align-items-center justify-content-center border-round" id="div_icone" >
                        <i class="pi pi-user text-xl" id="icone"></i>
                    </div>
                </div>

            </div>
        </div>
        <div class="col-12 lg:col-2 xl:col-3">
            <div class="card mb-0" id="cartao">
                <div class="flex justify-content-between mb-3">
                    <div>
                        <span class="block text-500 font-medium mb-3">
                            Campanhas Concluídas 
                        </span>
                        <div class="text-900 font-medium text-xl"></div>
                    </div>
                    <div class="flex align-items-center justify-content-center border-round" id="div_icone" >
                        <i class="pi pi-user text-xl" id="icone"></i>
                    </div>
                </div>
            </div>
        </div>
        

        <div class="col-12 xl:col-6">    
            <div class="card mb-0" id="cartao">
                <div class="flex justify-content-between align-items-center mb-5">
                    <h5></h5>
                    <div>
                    </div>
                </div>
            </div>
        </div>
        <div class="col-12 xl:col-6">    
            <div class="card mb-0" id="cartao">
                <div class="flex justify-content-between align-items-center mb-5">
                    <h5></h5>
                    <div>
                    </div>
                </div>
            </div>
        </div>
        <div class="col-12 xl:col-12">    
            <div class="card mb-0" id="cartao">
                <div class="flex justify-content-between align-items-center mb-5">
                    <h5></h5>
                    <div>
                    </div>
                </div>
            </div>    
        </div>
        <div class="col-12 lg:col-2 xl:col-3">
            <div class="card mb-0" id="cartao">
                <div class="flex justify-content-between mb-3">
                    <div>
                        <span class="block text-500 font-medium mb-3">
                         Os candidatos precisam recrutar  
                        </span>
                    </div>
                    <div class="flex align-items-center justify-content-center border-round" id="div_icone" >
                        <i class="pi pi-user text-xl" id="icone"></i>
                    </div>
                </div>
            </div>
        </div>
        <div class="col-12 lg:col-2 xl:col-3">
            <div class="card mb-0" id="cartao">
                <div class="flex justify-content-between mb-3">
                    <div>
                        <span class="block text-500 font-medium mb-3">
                            Candidatos recrutados 
                        </span>
                        <div class="text-900 font-medium text-xl"></div>
                    </div>
                    <div class="flex align-items-center justify-content-center border-round" id="div_icone" >
                        <i class="pi pi-user text-xl" id="icone"></i>
                    </div>
                </div>
            </div>
        </div>
        <div class="col-12 lg:col-2 xl:col-3" >
            <div class="card mb-0" id="cartao">
                <div class="flex justify-content-between mb-3">
                    <div>
                        <span class="block text-500 font-medium mb-3">
                            Próxima entrevista 
                        </span>
                        <div class="text-900 font-medium text-xl"></div>
                    </div>
                    <div class="flex align-items-center justify-content-center border-round" id="div_icone" >
                        <i class="pi pi-user text-xl" id="icone"></i>
                    </div>
                </div>

            </div>
        </div>
        <div class="col-12 lg:col-2 xl:col-3">
            <div class="card mb-0" id="cartao">
                <div class="flex justify-content-between mb-3">
                    <div>
                        <span class="block text-500 font-medium mb-3">
                            Campanhas em execução 
                        </span>
                        <div class="text-900 font-medium text-xl"></div>
                    </div>
                    <div class="flex align-items-center justify-content-center border-round" id="div_icone" >
                        <i class="pi pi-user text-xl" id="icone"></i>
                    </div>
                </div>
            </div>
        </div>

        
    </div>
</template>
