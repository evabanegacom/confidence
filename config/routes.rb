Rails.application.routes.draw do
  #get 'users/index'
  devise_for :users, :controllers => { registrations: 'registrations'}
  match '/users',   to: 'users#index',   via: 'get'
  match '/users/:id',     to: 'users#show',       via: 'get'
  resources :users, :only =>[:show]
  resources :tweets
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
  root'tweets#index'
end
