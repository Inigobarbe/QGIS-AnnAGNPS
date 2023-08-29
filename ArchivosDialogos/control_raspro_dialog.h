#ifndef CONTROL_RASPRO_DIALOG_H
#define CONTROL_RASPRO_DIALOG_H

#include <QDialog>

namespace Ui {
class control_raspro_dialog;
}

class control_raspro_dialog : public QDialog
{
    Q_OBJECT

public:
    explicit control_raspro_dialog(QWidget *parent = nullptr);
    ~control_raspro_dialog();

private:
    Ui::control_raspro_dialog *ui;
};

#endif // CONTROL_RASPRO_DIALOG_H
