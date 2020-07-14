class RegistrationsController < Devise::RegistrationsController
    private
  
    def sign_up_params
      params.require(:user).permit(:name, :password, :password_confirmation, :email, :phone_number)
    end
  
    def acount_update_params 
      params.require(:user).permit(:name, :username, :email, :password, :password_confirmation, :current_password, :phone_number)
    end  
end