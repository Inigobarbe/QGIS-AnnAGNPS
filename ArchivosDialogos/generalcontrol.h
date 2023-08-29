#ifndef GENERALCONTROL_H
#define GENERALCONTROL_H

#include <QDialog>

namespace Ui {
class GeneralControl;
}

class GeneralControl : public QDialog
{
    Q_OBJECT

public:
    explicit GeneralControl(QWidget *parent = nullptr);
    ~GeneralControl();

private:
    Ui::GeneralControl *ui;
};

#endif // GENERALCONTROL_H
