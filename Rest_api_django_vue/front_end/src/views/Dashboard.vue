<script setup>
import { onMounted, reactive, ref, watch } from 'vue';
import { ProductService } from '@/service/ProductService';
import { useLayout } from '@/layout/composables/layout';
import '@/assets/styles.scss';

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
const breadcrumbItems = ref([{ label: 'Home' }, { label: 'Dashboard' }]);
 
</script>

<template>
    <div class="grid">
        <div class="col-12 lg:col-2 xl:col-12">
            <Breadcrumb :home="breadcrumbHome" :model="breadcrumbItems" id="breadcrumb"/>
        </div>
        <div class="col-12 lg:col-2 xl:col-3">
            <div class="card mb-0" id="cartoes">
                <div class="flex justify-content-between mb-3">
                    <div>
                        <span class="block text-500 font-medium mb-3">
                        Recrutamento e Seleção
                        </span>
                    </div>
                    <div class="flex align-items-center justify-content-center border-round" style="width: 2.5rem; height: 2.5rem; background-color:#0077B6;" >
                        <i class="pi pi-folder text-xl" style="color:#fff;"></i>
                    </div>
                </div>
            </div>
        </div>
        <div class="col-12 lg:col-2 xl:col-3">
            <div class="card mb-0" id="cartoes">
                <div class="flex justify-content-between mb-3">
                    <div>
                        <span class="block text-500 font-medium mb-3">
                            Gestão da Integração
                        </span>
                        <div class="text-900 font-medium text-xl"></div>
                    </div>
                    <div class="flex align-items-center justify-content-center border-round" style="width: 2.5rem; height: 2.5rem; background-color:#0077B6;" >
                        <i class="pi pi-folder text-xl" style="color:#fff;"></i>
                    </div>
                </div>
            </div>
        </div>
        <div class="col-12 lg:col-2 xl:col-3" >
            <div class="card mb-0" id="cartoes">
                <div class="flex justify-content-between mb-3">
                    <div>
                        <span class="block text-500 font-medium mb-3">
                            TD-Políticas da Empresa
                        </span>
                        <div class="text-900 font-medium text-xl"></div>
                    </div>
                    <div class="flex align-items-center justify-content-center border-round" style="width: 2.5rem; height: 2.5rem; background-color:#0077B6;" >
                        <i class="pi pi-folder text-xl" style="color:#fff;"></i>
                    </div>
                </div>

            </div>
        </div>
        <div class="col-12 lg:col-2 xl:col-3">
            <div class="card mb-0" id="cartoes">
                <div class="flex justify-content-between mb-3">
                    <div>
                        <span class="block text-500 font-medium mb-3">
                            Gestão do Desenvolvimento Individual
                        </span>
                        <div class="text-900 font-medium text-xl"></div>
                    </div>
                    <div class="flex align-items-center justify-content-center border-round" style="width: 2.5rem; height: 2.5rem; background-color:#0077B6;" >
                        <i class="pi pi-folder text-xl" style="color:#fff;"></i>
                    </div>
                </div>
            </div>
        </div>
        <div class="col-12 lg:col-2 xl:col-3">
            <div class="card mb-0" id="cartoes">
                <div class="flex justify-content-between mb-3">
                    <div>
                        <span class="block text-500 font-medium mb-3">
                            Gestão de Plano de Sucessão e Liderança
                        </span>
                        <div class="text-900 font-medium text-xl"></div>
                    </div>
                    <div class="flex align-items-center justify-content-center border-round" style="width: 2.5rem; height: 2.5rem; background-color:#0077B6;" >
                        <i class="pi pi-folder text-xl" style="color:#fff;"></i>
                    </div>
                </div>
                <span class="text-green-500 font-medium"></span>
                <span class="text-500"></span>
            </div>
        </div>
        <div class="col-12 lg:col-2 xl:col-3">
            <div class="card mb-0" id="cartoes">
                <div class="flex justify-content-between mb-3">
                    <div>
                        <span class="block text-500 font-medium mb-3">
                        Gestão de Remunerações
                        </span>
                        <div class="text-900 font-medium text-xl"></div>
                    </div>
                    <div class="flex align-items-center justify-content-center border-round" style="width: 2.5rem; height: 2.5rem; background-color:#0077B6;" >
                        <i class="pi pi-folder text-xl" style="color:#fff;"></i>
                    </div>
                </div>
            </div>
        </div>  
        <div class="col-12 lg:col-2 xl:col-3">
            <div class="card mb-0" id="cartoes">
                <div class="flex justify-content-between mb-3">
                    <div>
                        <span class="block text-500 font-medium mb-3">Gestão Documental</span>
                        <div class="text-900 font-medium text-xl"></div>
                    </div>
                    <div class="flex align-items-center justify-content-center border-round" style="width: 2.5rem; height: 2.5rem; background-color:#0077B6;" >
                        <i class="pi pi-folder text-xl" style="color:#fff;"></i>
                    </div>
                </div>
            </div>
        </div>
        <div class="col-12 lg:col-2 xl:col-3">
            <div class="card mb-0" id="cartoes">
                <div class="flex justify-content-between mb-3">
                    <div>
                        <span class="block text-500 font-medium mb-3">Gestão de Assiduidade e Férias</span>
                        <div class="text-900 font-medium text-xl"></div>
                    </div>
                    <div class="flex align-items-center justify-content-center border-round" style="width: 2.5rem; height: 2.5rem; background-color:#0077B6;" >
                        <i class="pi pi-folder text-xl" style="color:#fff;"></i>
                    </div>
                </div>
            </div>
        </div>
        <div class="col-12 lg:col-2 xl:col-3">
            <div class="card mb-0" id="cartoes">
                <div class="flex justify-content-between mb-3">
                    <div>
                        <span class="block text-500 font-medium mb-3">Produção de Relatórios e Dashboard</span>
                        <div class="text-900 font-medium text-xl"></div>
                    </div>
                    <div class="flex align-items-center justify-content-center border-round" style="width: 2.5rem; height: 2.5rem; background-color:#0077B6;" >
                        <i class="pi pi-folder text-xl" style="color:#fff;"></i>
                    </div>
                </div>
            </div>
        </div>
        <div class="col-12 lg:col-2 xl:col-3">
            <div class="card mb-0" id="cartoes">
                <div class="flex justify-content-between mb-3">
                    <div>
                        <span class="block text-500 font-medium mb-3">Planeamento de Força de Trabalho</span>
                        <div class="text-900 font-medium text-xl"></div>
                    </div>
                    <div class="flex align-items-center justify-content-center border-round" style="width: 2.5rem; height: 2.5rem; background-color:#0077B6;" >
                        <i class="pi pi-folder text-xl" style="color:#fff;"></i>
                    </div>
                </div>
            </div>
        </div>
        <div class="col-12 lg:col-2 xl:col-3">
            <div class="card mb-0" id="cartoes">
                <div class="flex justify-content-between mb-3">
                    <div>
                        <span class="block text-500 font-medium mb-3">Engajamento de Talentos</span>
                        <div class="text-900 font-medium text-xl"></div>
                    </div>
                    <div class="flex align-items-center justify-content-center border-round" style="width: 2.5rem; height: 2.5rem; background-color:#0077B6;" >
                        <i class="pi pi-folder text-xl" style="color:#fff;"></i>
                    </div>
                </div>
            </div>
        </div>
        <div class="col-12 lg:col-2 xl:col-3">
            <div class="card mb-0" id="cartoes">
                <div class="flex justify-content-between mb-3">
                    <div>
                        <span class="block text-500 font-medium mb-3">Gestão de Viagem</span>
                        <div class="text-900 font-medium text-xl"></div>
                    </div>
                    <div class="flex align-items-center justify-content-center border-round" style="width: 2.5rem; height: 2.5rem; background-color:#0077B6;" >
                        <i class="pi pi-folder text-xl" style="color:#fff;"></i>
                    </div>
                </div>
            </div>
        </div> 
        <div class="col-12 lg:col-2 xl:col-3">
            <div class="card mb-0" id="cartoes">
                <div class="flex justify-content-between mb-3">
                    <div>
                        <span class="block text-500 font-medium mb-3">Gestão da Formação</span>
                        <div class="text-900 font-medium text-xl"> </div>
                    </div>
                    <div class="flex align-items-center justify-content-center border-round" style="width: 2.5rem; height: 2.5rem; background-color:#0077B6;" >
                        <i class="pi pi-folder text-xl" style="color:#fff;"></i>
                    </div>
                </div>
            </div>
        </div>
        <div class="col-12 lg:col-2 xl:col-10">
        </div>

        <div class="col-12 xl:col-4">    
            <div class="card mb-0" id="cartoes">
                <div class="flex justify-content-between align-items-center mb-5">
                    <h5></h5>
                    <div>
                    </div>
                </div>
            </div>
        </div>
        <div class="col-12 xl:col-4">    
            <div class="card mb-0" id="cartoes">
                <div class="flex justify-content-between align-items-center mb-5">
                    <h5></h5>
                    <div>

                    </div>
                </div>
            </div>
        </div>
        <div class="col-12 xl:col-4">    
            <div class="card mb-0" id="cartoes">
                <div class="flex justify-content-between align-items-center mb-5">
                    <h5></h5>
                    <div>
                    </div>
                </div>
            </div>
            
        </div>
        
    </div>
</template>
