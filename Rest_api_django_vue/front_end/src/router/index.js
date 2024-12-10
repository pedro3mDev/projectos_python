import { createRouter, createWebHistory } from 'vue-router';
import AppLayout from '@/layout/AppLayout.vue';

const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/landing',
            name: 'landing',
            component: () => import('@/views/Landing.vue')
        },
        {
            path: '/auth/login',
            name: 'login', 
            component: () => import('@/views/auth/Login.vue')
        },
        {
            path: '/auth/recuperarSenha',
            name: 'recuperarSenha',
            component: () => import('@/views/auth/RecuperarSenha.vue')
        },

        {
            path: '/',
            component: AppLayout,
            children: [
                {
                    path: '/',
                    name: 'dashboard',
                    component: () => import('@/views/Dashboard.vue')
                },
                {
                    path: '/user/perfil',
                    name: 'perfil_usuario',
                    component: () => import('@/views/Perfil.vue')
                },
                {
                    path: '/definicoes',
                    name: 'definicoes',
                    component: () => import('@/views/Definicoes.vue')
                },
                {
                    path: '/ajuda',
                    name: 'ajuda',
                    component: () => import('@/views/Ajuda.vue')
                },

                /*  Recrutamento e Selecção*/
                {
                    path: '/recutamento/painel',
                    name: 'painel_recurtamento',
                    component: () => import('@/views/mod_recrutamento/Painel.vue')
                },
                {
                    path: '/recutamento/campanha',
                    name: 'campanha_recurtamento',
                    component: () => import('@/views/mod_recrutamento/Campanha.vue')
                },
                {
                    path: '/recutamento/programarEntrevista',
                    name: 'campanha_programar_entrevista',
                    component: () => import('@/views/mod_recrutamento/ProgramarEntrevista.vue')
                },
                {
                    path: '/recutamento/candidato',
                    name: 'campanha_candidato',
                    component: () => import('@/views/mod_recrutamento/Candidato.vue')
                },
                

                /*  **************************** */
                
                
                

                
            ]
        }


    ]
});

export default router;
