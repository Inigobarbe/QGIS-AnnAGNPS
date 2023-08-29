#include "control_raspro_dialog.h"
#include "ui_control_raspro_dialog.h"

control_raspro_dialog::control_raspro_dialog(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::control_raspro_dialog)
{
    ui->setupUi(this);
}

control_raspro_dialog::~control_raspro_dialog()
{
    delete ui;
}
